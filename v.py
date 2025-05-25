import matplotlib.pyplot as plt
import numpy as np

# System specs
RAM_GB = 32
CPU_CORES = 12

# File sizes: 9 MB to 180 MB (20 samples)
file_sizes_mb = np.arange(9, 181, 9)  # [9, 18, 27, ..., 180]

# Random seed for reproducibility
np.random.seed(42)

# Simulate copy times (in seconds) with increased randomness
# Baseline: No driver, optimized for 12 cores and 32 GB RAM
base_speed = 500  # MB/s (approximate for SSD with multi-core optimization)
no_driver_time = file_sizes_mb / base_speed
no_driver_noise = np.random.normal(0, 0.2 * no_driver_time, no_driver_time.shape)
no_driver_time = np.maximum(no_driver_time + no_driver_noise, 0)  # Ensure non-negative

# Driver with linked list: significantly slower, non-linear scaling
linked_list_speed = base_speed / 10  # 50 MB/s
linked_list_base_time = file_sizes_mb / linked_list_speed
linked_list_overhead = 0.0005 * file_sizes_mb/10 ** 2  # Quadratic scaling
linked_list_time = linked_list_base_time + linked_list_overhead
linked_list_noise = np.random.normal(0, 0.2 * linked_list_time, linked_list_time.shape)
linked_list_time = np.maximum(linked_list_time + linked_list_noise, 0)

# Driver with vectors: slightly farther from no driver, with increased noise
vector_speed = base_speed * 0.95  # 95% of base speed (slightly slower than before)
vector_base_time = file_sizes_mb / vector_speed
vector_overhead = 0.015  # Increased overhead (15ms)
vector_time = vector_base_time + vector_overhead
vector_noise = np.random.normal(0.05 * vector_time, 0.1 * vector_time, vector_time.shape)
vector_time = np.maximum(vector_time + vector_noise, 0)

# Set modern style
plt.style.use('ggplot')  # Use ggplot style (built-in)
plt.figure(figsize=(12, 7), facecolor='#F7F7F7')  # Slightly larger figure with light background
ax = plt.gca()
ax.set_facecolor('#F7F7F7')  # Light background for the plot area

# Plot with updated, contrasted colors
plt.plot(file_sizes_mb, no_driver_time, color='#1E88E5', linestyle='-', linewidth=2.5, alpha=0.8, marker='o', markersize=5, label='No Driver')
plt.plot(file_sizes_mb, linked_list_time, color='#D32F2F', linestyle='-', linewidth=2.5, alpha=0.8, marker='o', markersize=5, label='Driver with Linked List')
plt.plot(file_sizes_mb, vector_time, color='#43A047', linestyle='-', linewidth=2.5, alpha=0.8, marker='o', markersize=5, label='Driver with Vectors')

# Customize title and labels
plt.title('File Copy Time vs File Size (32 GB RAM, 12 CPU Cores)', fontsize=16, pad=20, fontweight='bold', color='#333333')
plt.xlabel('File Size (MB)', fontsize=14, color='#333333')
plt.ylabel('Time (seconds)', fontsize=14, color='#333333')

# Customize grid and spines
plt.grid(True, linestyle='--', alpha=0.6, color='#BBBBBB')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#333333')
ax.spines['bottom'].set_color('#333333')
ax.tick_params(axis='both', which='major', labelsize=12, colors='#333333')

# Customize legend
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=12, frameon=True, shadow=True, facecolor='#FFFFFF', edgecolor='#333333')

# Adjust layout to prevent clipping
plt.tight_layout()

# Save plot
plt.savefig('file_copy_time_plot.png', dpi=300, bbox_inches='tight')
