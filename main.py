from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
from qiskit import QuantumCircuit, transpile, assemble
import matplotlib.pyplot as plt
from qiskit.result import marginal_counts

# Create a Quantum Circuit with 3 qubits and 3 classical bits
qc = QuantumCircuit(3, 3)

# Create an entangled pair between Alice and Bob
qc.h(1)
qc.cx(1, 2)
qc.barrier()

# Alice applies teleportation steps
qc.cx(0, 1)
qc.h(0)
qc.measure(0, 0)  # Measure Alice's qubit
qc.measure(1, 1)  # Measure entangled qubit

# Bob applies correction based on Alice's classical bits
qc.cx(1, 2)
qc.cz(0, 2)

# Measure Bob's qubit to check if teleportation worked
qc.measure(2, 2)

# Simulate the circuit
simulator = Aer.get_backend('qasm_simulator')
compiled_circuit = transpile(qc, simulator)
job = simulator.run(compiled_circuit)
result = job.result()

# Extract and plot results
marginal_result = marginal_counts(result.get_counts(), indices=[2])
print(marginal_result)
plot_histogram(marginal_result)

# Draw the circuit
qc.draw(output='mpl')
plt.show()
