def write(fp, points):
    if not points:
        return
    
    x, y = points[0]
    data = 'M{},{} ' .format(x, y)
    for p in points[1:]:
        x, y = p
        data += 'L{},{} ' .format(x, y)
    data += 'Z'  # Agrega el comando 'Z' al final para cerrar el trazado
    fp.write('<path d="{}" fill="Black" stroke="none" />\n'.format(data))


def export(geo, xsize, ysize, filename):
    with open(filename, 'w') as fp:
        fp.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        fp.write('<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{}" height="{}" >\n'.format(xsize, ysize))
        fp.write('<defs>\n')
        fp.write('</defs>\n')
        for points in geo:
            print(points)
            write(fp, points)   
        fp.write('</svg>')