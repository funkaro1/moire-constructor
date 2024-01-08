import shapely 

def intersect(a, b): #lets define that b is always the box
    poly1 = shapely.geometry.Polygon(a)
    poly2 = shapely.geometry.Polygon(b)
    intersection = poly1.intersection(poly2)
    if poly1.intersects(poly2) == False:
        return [False]        
    else:
        return [list(intersection.exterior.coords)]