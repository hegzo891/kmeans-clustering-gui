import tkinter as tk
from tkinter import filedialog, messagebox

from utils.file_handler import FileHandler
from utils.preprocessing import Preprocessor
from core.kmeans import KMeans
from core.outliers import OutlierDetector

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Mall Customers Clustering")

        self.file_path = None

        tk.Button(root, text="Select Mall Dataset", command=self.select_file).pack()

        tk.Label(root, text="Percentage (%)").pack()
        self.percent = tk.Entry(root)
        self.percent.pack()

        tk.Label(root, text="Number of Clusters (K)").pack()
        self.k = tk.Entry(root)
        self.k.pack()

        tk.Button(root, text="Run Clustering", command=self.run).pack()

        self.output = tk.Text(root, height=25, width=80)
        self.output.pack()

    def select_file(self):
        self.file_path = filedialog.askopenfilename()

    def run(self):
        if not self.file_path:
            messagebox.showerror("Error", "Select dataset")
            return

        try:
            percent = float(self.percent.get())
            k = int(self.k.get())
        except:
            messagebox.showerror("Error", "Invalid input")
            return

        # Load dataset
        handler = FileHandler(self.file_path)
        df = handler.load(percent)

        data = df.values

        # Normalize
        data = Preprocessor.normalize(data)

        # KMeans
        kmeans = KMeans(k)
        clusters = kmeans.fit(data)

        # Outliers
        detector = OutlierDetector()
        outliers = detector.detect(data, clusters, kmeans.centroids)

        # Display results
        self.output.delete(1.0, tk.END)

        for i in range(k):
            self.output.insert(tk.END, f"\n=== Cluster {i} ===\n")
            self.output.insert(tk.END, str(df[clusters == i]) + "\n")

        self.output.insert(tk.END, "\n=== Outliers ===\n")

        for i in outliers:
            self.output.insert(tk.END, f"\nOutlier in Cluster {clusters[i]}:\n")
            self.output.insert(tk.END, str(df.iloc[i]) + "\n")