import time
import sys
import subprocess
import os
import signal

def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        sys.exit(1)

def clear_output_file():
    output_file = "output.txt"
    if os.path.exists(output_file):
        with open(output_file, "w") as file:
            file.write("")

def handle_interrupt(sig, frame):
    print("KeyboardInterrupt: Stopping...")
    clear_output_file()
    sys.exit(1)

if __name__ == "__main__":
    # Register the signal handler for KeyboardInterrupt
    signal.signal(signal.SIGINT, handle_interrupt)

    # Your command for training
    train_command = "python train.py config/train_german-news_char.py --device=cpu --compile=False --eval_iters=20 --log_interval=10 --block_size=64 --batch_size=12 --n_layer=5 --n_head=5 --n_embd=240 --max_iters=2000 --lr_decay_iters=2000 --dropout=0.0"

    # Your command for plotting
    plot_command = "python plot.py"

    # Run train command
    train_process = subprocess.Popen(train_command, shell=True)

    try:
        while train_process.poll() is None:  # Check if train process is still running
            time.sleep(5)  # Wait for 15 seconds
            subprocess.run(plot_command, shell=True, check=True)  # Run plot command
    except KeyboardInterrupt:
        handle_interrupt(signal.SIGINT, None)
    finally:
        # Clear output.txt
        output_file = "output.txt"
        if os.path.exists(output_file):
            with open(output_file, "w") as file:
                file.write("")   


#python sample.py --out_dir=out-german-news-char --device=cpu