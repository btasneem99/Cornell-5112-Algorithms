def linear_search(packages, boxes):
    
    opt_wasted_space = float('inf')

    for supp_boxes in boxes:
        sorted_boxes = sorted(supp_boxes)
        curr_wasted_space = 0

        for pkg_size in packages:
            suitable_box_found = False
            for box_size in sorted_boxes:
                if box_size >= pkg_size:
                    curr_wasted_space += box_size - pkg_size
                    suitable_box_found = True
                    break

            if not suitable_box_found:
                curr_wasted_space = float('inf')
                break

        if curr_wasted_space < opt_wasted_space:
            opt_wasted_space = curr_wasted_space

    return opt_wasted_space if opt_wasted_space != float('inf') else -1