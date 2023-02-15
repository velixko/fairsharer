def fair_sharer(values, num_iterations, share=0.1):

    for i in range(num_iterations):
        max_idx = values.index(max(values))
        max_value = values[max_idx]
        if max_idx == 0:  # Left boundary
            values[1] += max_value * share
            values[-1] += max_value * share
        elif max_idx == len(values) - 1:  # Right boundary
            values[0] += max_value * share
            values[-2] += max_value * share
        else:  # Middle values
            values[max_idx-1] += max_value * share
            values[max_idx+1] += max_value * share
        values[max_idx] -= max_value * share

    return values
