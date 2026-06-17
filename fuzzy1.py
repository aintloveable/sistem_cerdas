import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 4, 100)

tidak_layak = np.piecewise(
    x,
    [x <= 1.5, (x > 1.5) & (x < 2.5), x >= 2.5],
    [1, lambda x: (2.5 - x), 0]
)

dipertimbangkan = np.piecewise(
    x,
    [x <= 1.5,
     (x > 1.5) & (x <= 2.5),
     (x > 2.5) & (x < 3.5),
     x >= 3.5],
    [0,
     lambda x: (x - 1.5),
     lambda x: (3.5 - x),
     0]
)

layak = np.piecewise(
    x,
    [x <= 2.5, (x > 2.5) & (x < 3.5), x >= 3.5],
    [0, lambda x: (x - 2.5), 1]
)

plt.plot(x, tidak_layak, label="Tidak Layak")
plt.plot(x, dipertimbangkan, label="Dipertimbangkan")
plt.plot(x, layak, label="Layak")

plt.xlabel("IPK")
plt.ylabel("Derajat Keanggotaan")
plt.title("Fuzzy Kelayakan Beasiswa")
plt.legend()
plt.grid(True)
plt.show()
