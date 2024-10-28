# Programming Assignments 
Part of Data Structures and Algorithms course at IIT Delhi (2022-23 Semester I)

## a1: Drone Movement

### Objective:
The task is to simulate the movement of a drone based on a series of commands. The drone can move in three dimensions (X, Y, Z) with basic movements such as +X, -X, +Y, -Y, +Z, and -Z. The goal is to determine the final position of the drone and the total distance traveled after executing a given program.

### Algorithm Used:
This program implements a **Stack-based algorithm** to efficiently handle nested commands. The stack is used to manage the recursive nature of instructions like `m(P)`, where a sub-program `P` needs to be executed `m` times. The program processes the string in O(n) time, utilizing the stack to keep track of positions and operations in nested loops.

---

## a2: Elastic Collisions

### Objective:
The objective of this assignment is to simulate elastic collisions in a one-dimensional space. Given the mass, position, and velocity of `n` point masses, the program computes the collisions in a chronological order and returns them until either `m` collisions are recorded or time `T` is reached.

### Algorithm Used:
The **Event-Driven Simulation** algorithm is implemented to model the collisions between the objects. Using Newton’s law for elastic collisions, the program maintains the system's energy and momentum. The algorithm efficiently sorts collisions using a priority queue, running in **O(n + m log n)** time, where `n` is the number of objects, and `m` is the number of collisions.

---

## a3: Search Nearby Points

### Objective:
This assignment focuses on creating a data structure that stores 2D points and allows efficient querying for points within a certain ℓ∞-distance from a given query point thus, emulating search nearby feature of Google Maps

### Algorithm Used:
The program uses a **Divide-and-Conquer** approach to preprocess the data points into a balanced search structure (like a KD-tree). The preprocessing step takes **O(n log n)** time, where `n` is the number of points. Searching for nearby points within a distance `d` is done in **O(m + log² n)** time, where `m` is the number of points returned, and `n` is the number of stored points. This approach ensures fast and efficient searching for points near a given query.

---

## a4: Pattern Matching

### Objective:
The objective is to implement an algorithm that searches for occurrences of a pattern in a document, with strict memory constraints of O(1). The program should use O(log m + log n) working memory and should also handle wildcards in the pattern with a small probability of false positives.

### Algorithm Used:
The **Rabin-Karp Algorithm** is utilized for pattern matching with a twist. Instead of directly comparing strings, the program computes hash values (modulo a large prime) to reduce space complexity. The algorithm uses modular arithmetic to compare the pattern and the document's substrings, achieving the goal in **O((m + n) log q)** time. Wildcards are managed using a variation of the same hash-based approach, allowing flexible pattern matching with limited memory usage.

---

## a5: Maximum Packet Size in a Network

### Objective:
The goal is to find the maximum packet size that can be transferred between two routers in a computer network. Given a set of routers and links between them with specified capacities, the program determines the largest possible packet that can be transferred between two specified routers.

### Algorithm Used:
The program implements a **Maximum Bottleneck Path Algorithm** (similar to Dijkstra's algorithm but focused on the maximum edge weight). A priority queue is used to explore paths in the network, always choosing the path with the highest possible minimum capacity. The algorithm runs in **O(m log m)** time, where `m` is the number of links in the network.
