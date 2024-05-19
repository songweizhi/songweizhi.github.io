import os


def sep_path_basename_ext(file_in):

    f_path, file_name = os.path.split(file_in)
    if f_path == '':
        f_path = '.'
    f_base, f_ext = os.path.splitext(file_name)

    return f_path, f_base, f_ext


########################################################################################################################

photo_list_txt = 'photo_list.txt'
photos_md_main = '../../photos.md'

########################################################################################################################

# read in photo_list_txt
main_page_group_order_list = []
page_to_photo_dict = dict()
added_to_main_page_set = set()
for each_line in open(photo_list_txt):
    each_line_split = each_line.strip().split('\t')
    print(each_line_split)
    photo_group = each_line_split[0]
    photo_page  = each_line_split[1]
    photo_title = each_line_split[2]
    photo_loci  = each_line_split[3]

    # added group to group_order_list if not added yet
    if photo_group not in main_page_group_order_list:
        main_page_group_order_list.append(photo_group)

    if 'main' not in page_to_photo_dict:
        page_to_photo_dict['main'] = dict()

    if photo_group not in page_to_photo_dict['main']:
        page_to_photo_dict['main'][photo_group] = []

    if photo_page == 'main':
        page_to_photo_dict['main'][photo_group].append(each_line_split)
    else:
        if photo_page not in added_to_main_page_set:
            page_to_photo_dict['main'][photo_group].append(each_line_split)
            added_to_main_page_set.add(photo_page)
            page_to_photo_dict[photo_page] = [each_line_split]
        else:
            page_to_photo_dict[photo_page].append(each_line_split)

# write out md files
for each_page in page_to_photo_dict:
    if each_page == 'main':
        main_page_photo_dict = page_to_photo_dict[each_page]
        photos_md_main_handle = open(photos_md_main, 'w')
        photos_md_main_handle.write('---\ntitle: Photos\n---\n\n\n')
        for each_group in main_page_photo_dict:
            photos_md_main_handle.write('### %s\n' % each_group)
            if each_group == 'Taiwan (2017)':
                photos_md_main_handle.write('\nBest wishes to Taiwan. I also wish for every individual in the Greater China Area a peaceful and dignified life (January 13th, 2024).\n\n')
            photos_md_main_handle.write('<div id="banner">\n')
            group_photo_list = main_page_photo_dict[each_group]
            for each_photo in group_photo_list:
                photo_page  = each_photo[1]
                photo_title = each_photo[2]
                photo_file  = each_photo[3]
                photo_file_no_ext = '.'.join(photo_file.split('.')[:-1])
                if photo_page == 'main':
                    photos_md_main_handle.write('\t<div class="inline-block" style="display:inline-block;"><a href="%s"><img src="%s" style="height: 120px;"></a><div><p>%s</p></div></div>\n' % (photo_file, photo_file, photo_title))
                else:
                    photos_md_main_handle.write('\t<div class="inline-block" style="display:inline-block;"><a href="%s"><img src="%s" style="height: 120px;"></a><div><p>%s</p></div></div>\n' % (photo_file_no_ext, photo_file, photo_title))
            photos_md_main_handle.write('</div>\n\n\n')
        photos_md_main_handle.close()
    else:
        current_page_photo_list = page_to_photo_dict[each_page]
        cover_photo = current_page_photo_list[0]
        current_page_title = cover_photo[2]
        f_path, f_base, _ = sep_path_basename_ext(cover_photo[3])
        current_page_md = '%s/%s.md' % (f_path.replace('assets/photos/', ''), f_base)
        current_page_md_handle = open(current_page_md, 'w')
        current_page_md_handle.write('---\ntitle: %s\n---\n\n\n<div id="banner">\n' % current_page_title)
        for each_photo in current_page_photo_list:
            photo_page = each_photo[1]
            photo_title = each_photo[2]
            photo_file = each_photo[3]
            photo_file_no_path = photo_file.split('/')[-1]
            current_page_md_handle.write('\t<div class="inline-block" style="display:inline-block;"><a href="%s"><img src="%s" style="height: 180px;"></a><div><p>%s</p></div></div>\n' % (photo_file_no_path, photo_file_no_path, photo_title))
        current_page_md_handle.write('</div>\n\n\n')
        current_page_md_handle.close()

