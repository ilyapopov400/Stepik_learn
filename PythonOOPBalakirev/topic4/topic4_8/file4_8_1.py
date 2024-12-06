class Vertex:
    """
    - для представления вершин графа (на карте это могут быть: здания, остановки, достопримечательности и т.п.)
    """

    def __init__(self):
        self._links = list()  # - список связей с другими вершинами графа(список объектов класса Link)

    @property
    def links(self):
        return self._links


class Link:
    """
    - для описания связи между двумя произвольными вершинами графа (на карте: маршруты, время в пути и т.п.)
    """

    def __init__(self, v1: Vertex, v2: Vertex):
        self._v1 = v1
        self._v2 = v2
        self._dist = 1

    @property
    def v1(self):
        return self._v1

    @property
    def v2(self):
        return self._v2

    @property
    def dist(self):
        return self._dist

    # @dist.setter
    # def dist(self, data):
    #     self._dist = data


class LinkedGraph:
    """
    - для представления связного графа в целом (карта целиком)
    """

    def __init__(self):
        """
        _links - список из всех связей графа (из объектов класса Link);
        _vertex - список из всех вершин графа (из объектов класса Vertex);
        """
        self._links = list()
        self._vertex = list()

    def add_vertex(self, v):
        """
        - для добавления новой вершины v в список _vertex (если она там отсутствует)
        """
        if isinstance(v, Vertex) and v not in self._vertex:
            self._vertex.append(v)

    def add_link(self, link):
        """
        - для добавления новой связи link в список _links (если объект link с указанными вершинами в списке отсутствует)
        """
        if isinstance(link, Link):
            filt = filter(
                lambda x: (link.v1 == x.v1 and link.v2 == x.v2) or (link.v1 == x.v2 and link.v2 == x.v1), self._links
            )
            if not bool(tuple(filt)):
                self._links.append(link)

                self.add_vertex(link.v1)
                self.add_vertex(link.v2)

                link.v1.links.append(link)
                link.v2.links.append(link)

    def find_path(self, start_v, stop_v) -> tuple:
        """
        - для поиска кратчайшего маршрута из вершины start_v в вершину stop_v
        - должен возвращать список
            из вершин кратчайшего маршрута
            и список из связей этого же маршрута в виде кортежа
            ([вершины кратчайшего пути], [связи между вершинами])
        """
        self._start_v = start_v
        self._stop_v = stop_v
        return self._next(self._start_v, None, [], [])

    def _dist_path(self, links):
        return sum(
            [x.dist for x in links if x is not None]
        )

    def _next(self, current, link_prev, current_path, current_links):
        current_path += [current]
        if link_prev:
            current_links += [link_prev]

        if current == self._stop_v:
            return current_path, current_links

        len_path = -1
        best_path = []
        best_links = []
        for link in current.links:
            path = []
            links = []
            if link.v1 not in current_path:
                path, links = self._next(link.v1, link, current_path[:], current_links[:])
            elif link.v2 not in current_path:
                path, links = self._next(link.v2, link, current_path[:], current_links[:])

            if self._stop_v in path and (len_path > self._dist_path(links) or len_path == -1):
                len_path = self._dist_path(links)
                best_path = path[:]
                best_links = links[:]
        return best_path, best_links


class Station(Vertex):
    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def __repr__(self):
        return self.name


class LinkMetro(Link):
    def __init__(self, v1, v2, dist):
        super().__init__(v1, v2)
        self._dist = dist


if __name__ == "__main__":
    map2 = LinkedGraph()
    v1 = Vertex()
    v2 = Vertex()
    v3 = Vertex()
    v4 = Vertex()
    v5 = Vertex()
    map2.add_link(Link(v1, v2))
    map2.add_link(Link(v2, v3))
    map2.add_link(Link(v2, v4))
    map2.add_link(Link(v3, v4))
    map2.add_link(Link(v4, v5))
    assert len(map2._links) == 5, "неверное число связей в списке _links класса LinkedGraph"
    assert len(map2._vertex) == 5, "неверное число вершин в списке _vertex класса LinkedGraph"
    map2.add_link(Link(v2, v1))
    assert len(map2._links) == 5, "метод add_link() добавил связь Link(v2, v1), хотя уже имеется связь Link(v1, v2)"

    path = map2.find_path(v1, v5)

    s = sum([x.dist for x in path[1]])
    assert s == 3, "неверная суммарная длина маршрута, возможно, некорректно работает объект-свойство dist"

    assert issubclass(Station, Vertex) and issubclass(LinkMetro,
                                                      Link), "класс Station должен наследоваться от класса Vertex, а класс LinkMetro от класса Link"
    map2 = LinkedGraph()
    v1 = Station("1")
    v2 = Station("2")
    v3 = Station("3")
    v4 = Station("4")
    v5 = Station("5")
    map2.add_link(LinkMetro(v1, v2, 1))
    map2.add_link(LinkMetro(v2, v3, 2))
    map2.add_link(LinkMetro(v2, v4, 7))
    map2.add_link(LinkMetro(v3, v4, 3))
    map2.add_link(LinkMetro(v4, v5, 1))
    assert len(map2._links) == 5, "неверное число связей в списке _links класса LinkedGraph"
    assert len(map2._vertex) == 5, "неверное число вершин в списке _vertex класса LinkedGraph"
    path = map2.find_path(v1, v5)
    assert str(path[0]) == '[1, 2, 3, 4, 5]', path[0]
    s = sum([x.dist for x in path[1]])
    assert s == 7, "неверная суммарная длина маршрута для карты метро"
