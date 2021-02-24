# NetworkX

***`G`: 그래프 객체

`nx.Graph()`: 그래프 선언

`G.add_edge(v1, v2)`: 정점 간 간선을 생성. 정점이 없을 경우 그래프에 동시에 업데이트

`G.number_of_nodes/edges()`: 그래프 내 정점/간선 수

`nx.connected_components(G)`: 그래프 내 연결 요소별 정점을 담은 generator를 리턴

`nx.algorithms.community.modularity(G, communities) -> float`: 그래프 내 커뮤니티별 군집성 측정

`nx.edge_betweenness_centrality(G)`: 그래프 내 매개중심성 측정

`nx.spring_layout(G) -> dict` : 그래프의 정점과 간선의 불필요한 중첩을 최소화한 레이아웃 구성

`nx.draw_networkx_nodes(G, pos: dict, node_color: list) `: 그래프의 정점을 시각화 함

`nx.draw_networkx_nodes(G, pos: dict)`: 그래프의 간선을 시각화 함

`kernighan_lin_bisection(G)`: 그래프를 2개의 커뮤니티로 분류

`nx.algorithms.community.centrality.girvan_newman`: Girvan-Newman 알고리즘을 활용하여 커뮤니티 분류

`nx.algorithms.community.greedy_modularity_communities`: Girvan-Newman 알고리즘보다 빠르고 더 높은 군집성을 갖는 커뮤니티들로 분류

