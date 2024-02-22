import time
import sys
import subprocess

if __name__ == "__main__":
    start_time = time.time()

    # Your command
    command = "python train.py config/train_german-news_char.py --device=cpu --compile=False --eval_iters=20 --log_interval=1 --block_size=64 --batch_size=12 --n_layer=6 --n_head=6 --n_embd=240 --max_iters=2000 --lr_decay_iters=2000 --dropout=0.0"

    try:
        # Run the command
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        sys.exit(1)

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Execution time: {elapsed_time} seconds")
