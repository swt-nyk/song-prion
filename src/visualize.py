import matplotlib.pyplot as plt

def plot_protein_profile(protein_result: dict, output_image: str = "profile.png"):
    qn_scores = [w["qn_fraction"] for w in protein_result["qn_windows"]]
    papa_scores = [w["papa_score"] for w in protein_result["papa_windows"]]
    disorder_scores = [w["disorder_score"] for w in protein_result["disorder_windows"]]
    positions = [w["start"] for w in protein_result["qn_windows"]]

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(positions, qn_scores, label="Q/N Density", color="blue")
    ax.plot(positions, papa_scores, label="PAPA Score", color="red")
    ax.plot(positions, disorder_scores, label="Disorder Score", color="green")

    ax.set_xlabel("Sequence Position (Window Start)")
    ax.set_ylabel("Score")
    ax.set_title(f"Prion Domain Profile: {protein_result['id']}")
    ax.legend()
    ax.grid(True, linestyle="--", alpha=0.6)

    plt.tight_layout()
    plt.savefig(output_image, dpi=300)
    plt.close()
