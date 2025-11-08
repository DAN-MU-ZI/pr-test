def bfs(visited, x, y):
    queue = deque([(x, y)])
    visited[x][y] = True

    discount_list = []

    while queue:
        a, b = queue.popleft()
        sea_count = 0

        for dx, dy in directions:
            nx = a + dx
            ny = b + dy
            if 0 <= nx < n and 0 <= ny < m:
                if not arr[nx][ny]:
                    sea_count += 1
                elif not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = True

        if sea_count:
            discount_list.append((a, b, sea_count))

    while discount_list:
        a, b, count = discount_list.pop()
        arr[a][b] = max(arr[a][b] - count, 0)
