def binary_search(packages, boxes):
    def find_min_box_size(package_size, box_sizes):
        left, right = 0, len(box_sizes) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if box_sizes[mid] < package_size:
                left = mid + 1
            else:
                right = mid - 1
        return box_sizes[left] if left < len(box_sizes) else None

    opt_wasted_space = float('inf')

    for supplier_boxes in boxes:
        sorted_boxes = sorted(supplier_boxes)
        curr_wasted_space = 0

        for package_size in packages:
            min_box_size = find_min_box_size(package_size, sorted_boxes)
            if min_box_size is None:
                curr_wasted_space = float('inf')
                break
            else:
                curr_wasted_space += min_box_size - package_size

        if curr_wasted_space < opt_wasted_space:
            opt_wasted_space = curr_wasted_space

    return opt_wasted_space if opt_wasted_space != float('inf') else -1
