# Quantum-Teleportation

🧩 How It Works
1️⃣ Entanglement Setup: Alice and Bob first share an entangled Bell pair (a special quantum state).
2️⃣ Alice's Qubit: Alice has a third qubit (the one she wants to teleport). She performs a CNOT gate (to entangle her qubit with her entangled pair) and then a Hadamard gate to create an interference pattern.
3️⃣ Measurement & Communication: Alice measures her two qubits, collapsing them into a classical result (00, 01, 10, or 11). She then sends these two classical bits to Bob.
4️⃣ Bob's Quantum Correction: Based on Alice's classical bits, Bob applies the correct Pauli gate (I, X, Z, or XZ) to his qubit.
5️⃣ Boom! 🎉 The original qubit’s state now exists on Bob’s side, even though it was never physically sent.

⚡ Why Is It Cool?
You’re not "physically" sending the qubit, just its quantum state, which is insane! 🚀
It shows entanglement in action, proving that quantum mechanics is legit.
It’s a fundamental step towards quantum networks and quantum internet.
🛠 Qiskit Implementation
We can run this entire teleportation protocol using Qiskit, IBM’s quantum computing framework. It lets us simulate quantum circuits and even run them on real IBM Quantum computers.
