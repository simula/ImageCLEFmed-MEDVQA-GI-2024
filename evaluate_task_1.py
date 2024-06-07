import argparse
import numpy as np
from skimage import io
from tensorflow.keras.applications.inception_v3 import InceptionV3, preprocess_input
from tensorflow.keras.models import Model
from scipy.linalg import sqrtm
import os


def load_inception_model():
    model = InceptionV3()
    return Model(inputs=model.inputs, outputs=model.layers[-1].output)


def preprocess_images(image_paths):
    images = np.array(
        [
            preprocess_input(np.resize(io.imread(img), (299, 299, 3)))
            for img in image_paths
        ]
    )
    return images


def calculate_fid(real_images, generated_images, model):
    act1 = model.predict(real_images)
    act2 = model.predict(generated_images)
    mu1, sigma1 = act1.mean(axis=0), np.cov(act1, rowvar=False)
    mu2, sigma2 = act2.mean(axis=0), np.cov(act2, rowvar=False)
    ssdiff = np.sum((mu1 - mu2) ** 2.0)
    covmean = sqrtm(sigma1.dot(sigma2))
    if np.iscomplexobj(covmean):
        covmean = covmean.real
    fid = ssdiff + np.trace(sigma1 + sigma2 - 2.0 * covmean)
    return fid


def calculate_inception_score(images, model, n_split=10, eps=1e-16):
    yhat = model.predict(images)
    scores = []
    n_part = np.floor(len(yhat) / n_split)
    for i in range(n_split):
        ix_start, ix_end = int(i * n_part), int((i + 1) * n_part)
        p_yx = yhat[ix_start:ix_end]
        p_y = np.expand_dims(p_yx.mean(axis=0), axis=0)
        kl_div = p_yx * (np.log(p_yx + eps) - np.log(p_y + eps))
        sum_kl_div = kl_div.sum(axis=1)
        avg_kl_div = np.mean(sum_kl_div)
        is_score = np.exp(avg_kl_div)
        scores.append(is_score)
    is_avg, is_std, is_med = np.mean(scores), np.std(scores), np.median(scores)
    return is_avg, is_std, is_med, scores


def main(args):
    real_image_paths = [
        os.path.join(args.real_images, fname)
        for fname in os.listdir(args.real_images)
        if fname.endswith(("png", "jpg", "jpeg"))
    ]
    generated_image_paths = [
        os.path.join(args.generated_images, fname)
        for fname in os.listdir(args.generated_images)
        if fname.endswith(("png", "jpg", "jpeg"))
    ]

    real_images = preprocess_images(real_image_paths)
    generated_images = preprocess_images(generated_image_paths)

    model = load_inception_model()

    fid_score = calculate_fid(real_images, generated_images, model)
    is_avg, is_std, is_med, scores = calculate_inception_score(generated_images, model)

    task1_results = {
        "FID Score": fid_score,
        "Inception Score (avg)": is_avg,
        "Inception Score (std)": is_std,
        "Inception Score (med)": is_med,
    }

    if not os.path.exists(os.path.dirname(args.output_file)):
        os.makedirs(os.path.dirname(args.output_file))

    with open(args.output_file, "w") as f:
        f.write("Task 1: Image Synthesis Evaluation\n")
        for key, value in task1_results.items():
            f.write(f"{key}: {value}\n")

        f.write(f"\nScores per group\n")
        for i, score in enumerate(scores):
            f.write(f"Group {i+1}: {score}\n")

    print(f"Results saved to {args.output_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Evaluate Image Synthesis and Optimal Prompt Generation"
    )
    parser.add_argument(
        "--real_images",
        type=str,
        required=True,
        help="Directory containing real images",
    )
    parser.add_argument(
        "--generated_images",
        type=str,
        required=True,
        help="Directory containing generated images",
    )
    parser.add_argument(
        "--output_file", type=str, required=True, help="Output file to save the results"
    )

    args = parser.parse_args()
    main(args)
