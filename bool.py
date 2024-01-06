import shapely 

def intersect(a, b): #lets define that b is always the box
    poly1 = shapely.geometry.Polygon(a)
    poly2 = shapely.geometry.Polygon(b)
    intersection = poly2.intersection(poly1)
    if intersection.is_empty:
        return []
    elif isinstance(intersection, shapely.geometry.LineString):
        return [list(intersection.coords)]
    elif isinstance(intersection, shapely.geometry.Polygon):
        return [list(intersection.exterior.coords)]
    else:
        return [list(i.coords) for i in intersection]