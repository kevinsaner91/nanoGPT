import matplotlib.pyplot as plt

# Extracting training and validation loss values
train_losses = []
val_losses = []
iterations = []

log_file_path = "output.txt"  # Update with your log file path

with open(log_file_path, "r") as file:
    for line_num, line in enumerate(file):
        if "train loss" in line and "val loss" in line:  # Check for both train and val loss in the line
            try:
                train_loss = float(line.split("train loss ")[1].split(",")[0])
                val_loss = float(line.split("val loss ")[1].strip())
                train_losses.append(train_loss)
                val_losses.append(val_loss)
                iterations.append(int(line.split("step ")[1].split(":")[0]))
            except IndexError:
                print(f"Error processing line {line_num + 1}: {line.strip()}")

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(iterations, train_losses, label="Training Loss")
plt.plot(iterations, val_losses, label="Validation Loss")
plt.xlabel("Iteration")
plt.ylabel("Loss")
plt.title("Training and Validation Loss Over Iterations")
plt.xticks(range(0, iterations[-1] + 1, 100)) # Set x-axis ticks to match iteration numbers
plt.legend()
plt.grid(True)

# Save the plot as an image file
plt.savefig("loss_plot.png")
