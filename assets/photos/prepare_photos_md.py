

photo_list_txt  = 'photo_list.txt'
photos_md       = '../../photos.md'


photos_md_handle = open(photos_md, 'w')
photos_md_handle.write('---\ntitle: Photos\n---\n\n\n')


current_group = ''
for each_line in open(photo_list_txt):
    each_line_split = each_line.strip().split('\t')
    print(each_line_split)
    photo_group = each_line_split[0]
    photo_title = each_line_split[1]
    photo_loci  = each_line_split[2]
    if current_group == '':
        current_group = photo_group
        photos_md_handle.write('### %s\n' % current_group)
        photos_md_handle.write('<div id="banner">\n')
        photos_md_handle.write('\t<div class="inline-block" style="display:inline-block;"><a href="%s"><img src="%s" style="height: 120px;"></a><div><p>%s</p></div></div>\n' % (photo_loci, photo_loci, photo_title))
    elif photo_group == current_group:
        photos_md_handle.write('\t<div class="inline-block" style="display:inline-block;"><a href="%s"><img src="%s" style="height: 120px;"></a><div><p>%s</p></div></div>\n' % (photo_loci, photo_loci, photo_title))
    elif photo_group != current_group:
        photos_md_handle.write('</div>\n\n\n')
        current_group = photo_group
        photos_md_handle.write('### %s\n' % current_group)
        photos_md_handle.write('<div id="banner">\n')
        photos_md_handle.write('\t<div class="inline-block" style="display:inline-block;"><a href="%s"><img src="%s" style="height: 120px;"></a><div><p>%s</p></div></div>\n' % (photo_loci, photo_loci, photo_title))
photos_md_handle.write('</div>\n')
photos_md_handle.close()
