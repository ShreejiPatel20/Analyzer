import numpy as np


class DataAnalytics:

    total_analyzers_created = 0

    def __init__(self, data=None):
        self.__data = np.array(data) if data is not None else None
        DataAnalytics.total_analyzers_created += 1

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, new_data):
        self.__data = np.array(new_data)

    def __validate_data(self):
        if self.__data is None:
            raise ValueError("No array has been initialized yet. Please create an array first.")

    def index_element(self, indices):
        self.__validate_data()
        return self.__data[indices]

    def slice_array(self, slices):
        self.__validate_data()
        return self.__data[slices]

    def combine(self, other_array, axis=0):
        self.__validate_data()
        return np.vstack((self.__data, other_array)) if axis == 0 else np.hstack((self.__data, other_array))

    def split(self, sections, axis=0):
        self.__validate_data()
        return np.array_split(self.__data, sections, axis=axis)

    def add(self, other_array):
        self.__validate_data()
        return np.add(self.__data, other_array)

    def subtract(self, other_array):
        self.__validate_data()
        return np.subtract(self.__data, other_array)

    def multiply(self, other_array):
        self.__validate_data()
        return np.multiply(self.__data, other_array)

    def divide(self, other_array):
        self.__validate_data()
        return np.divide(self.__data, other_array)

    def dot_product(self, other_array):
        self.__validate_data()
        return np.dot(self.__data, other_array)

    def matrix_multiply(self, other_array):
        self.__validate_data()
        return np.matmul(self.__data, other_array)

    def search_value(self, value):
        self.__validate_data()
        return np.where(self.__data == value)

    def sort_array(self, axis=-1, ascending=True):
        self.__validate_data()
        sorted_arr = np.sort(self.__data, axis=axis)
        if not ascending:
            sorted_arr = np.flip(sorted_arr, axis=axis)
        return sorted_arr

    def filter_values(self, condition_str):
        self.__validate_data()
        mask = eval(f"self.data {condition_str}")
        return self.__data[mask]

    def get_sum(self):
        self.__validate_data()
        return np.sum(self.__data)

    def get_mean(self):
        self.__validate_data()
        return np.mean(self.__data)

    def get_median(self):
        self.__validate_data()
        return np.median(self.__data)

    def get_std(self):
        self.__validate_data()
        return np.std(self.__data)

    def get_variance(self):
        self.__validate_data()
        return np.var(self.__data)

    def get_min(self):
        self.__validate_data()
        return np.min(self.__data)

    def get_max(self):
        self.__validate_data()
        return np.max(self.__data)

    def get_percentile(self, q):
        self.__validate_data()
        return np.percentile(self.__data, q)

    def get_correlation(self, other_array):
        self.__validate_data()
        return np.corrcoef(self.__data.flatten(), other_array.flatten())

    @classmethod
    def get_instance_count(cls):
        return cls.total_analyzers_created

    @staticmethod
    def parse_range(range_str):
        parts = [int(p) if p.strip() else None for p in range_str.split(':')]
        if len(parts) == 1:
            return slice(parts[0], parts[0] + 1)
        elif len(parts) == 2:
            return slice(parts[0], parts[1])
        elif len(parts) == 3:
            return slice(parts[0], parts[1], parts[2])
        return slice(None)


def main():
    analyzer = DataAnalytics()

    print("Welcome to the NumPy Analyzer!")
    print("=" * 46)

    while True:
        print("\nChoose an option:")
        print("1. Create a Numpy Array")
        print("2. Perform Mathematical Operations")
        print("3. Combine or Split Arrays")
        print("4. Search, Sort, or Filter Arrays")
        print("5. Compute Aggregates and Statistics")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            print("\nSelect the type of array to create:")
            print("1. 1D Array")
            print("2. 2D Array")
            print("3. 3D Array")
            arr_type = input("Enter your choice: ").strip()

            if arr_type == '1':
                n = int(input("Enter number of elements: "))
                raw = input(f"Enter {n} elements separated by space: ")
                arr = np.array([float(x) if '.' in x else int(x) for x in raw.split()][:n])
                analyzer.data = arr
            elif arr_type == '2':
                rows = int(input("Enter the number of rows: "))
                cols = int(input("Enter the number of columns: "))
                total = rows * cols
                raw = input(f"Enter {total} elements for the array separated by space: ")
                values = [float(x) if '.' in x else int(x) for x in raw.split()][:total]
                analyzer.data = np.array(values).reshape((rows, cols))
            elif arr_type == '3':
                d1 = int(input("Enter dimension 1: "))
                d2 = int(input("Enter dimension 2 (rows): "))
                d3 = int(input("Enter dimension 3 (columns): "))
                total = d1 * d2 * d3
                raw = input(f"Enter {total} elements separated by space: ")
                values = [float(x) if '.' in x else int(x) for x in raw.split()][:total]
                analyzer.data = np.array(values).reshape((d1, d2, d3))
            else:
                print("Invalid option.")
                continue

            print("\nArray created successfully:")
            print(analyzer.data)

            while True:
                print("\nChoose an operation:")
                print("1. Indexing")
                print("2. Slicing")
                print("3. Go Back")
                sub_op = input("Enter your choice: ").strip()

                if sub_op == '1':
                    idx_str = input(f"Enter index as comma-separated integers (dimensions: {analyzer.data.ndim}): ")
                    indices = tuple(map(int, idx_str.split(',')))
                    print(f"Element at {indices}:", analyzer.index_element(indices))
                elif sub_op == '2':
                    if analyzer.data.ndim == 1:
                        r_str = input("Enter the range (start:end): ")
                        print("\nSliced Array:")
                        print(analyzer.slice_array(DataAnalytics.parse_range(r_str)))
                    elif analyzer.data.ndim == 2:
                        row_range = input("Enter the row range (start:end): ")
                        col_range = input("Enter the column range (start:end): ")
                        r_slice = DataAnalytics.parse_range(row_range)
                        c_slice = DataAnalytics.parse_range(col_range)
                        print("\nSliced Array:")
                        print(analyzer.slice_array((r_slice, c_slice)))
                    else:
                        print("Multi-dimensional slicing: apply across all axes.")
                elif sub_op == '3':
                    break

        elif choice == '2':
            if analyzer.data is None:
                print("Please create an array first!")
                continue

            print("\nChoose a mathematical operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Dot Product / Matrix Multiplication")
            op = input("Enter your choice: ").strip()

            total_elem = analyzer.data.size
            raw = input(f"\nEnter the same-size array elements ({total_elem} elements separated by space): ")
            vals = [float(x) if '.' in x else int(x) for x in raw.split()][:total_elem]
            second_arr = np.array(vals).reshape(analyzer.data.shape)

            print("\nOriginal Array:\n", analyzer.data)
            print("Second Array:\n", second_arr)

            if op == '1':
                print("\nResult of Addition:\n", analyzer.add(second_arr))
            elif op == '2':
                print("\nResult of Subtraction:\n", analyzer.subtract(second_arr))
            elif op == '3':
                print("\nResult of Multiplication:\n", analyzer.multiply(second_arr))
            elif op == '4':
                print("\nResult of Division:\n", analyzer.divide(second_arr))
            elif op == '5':
                if analyzer.data.ndim == 2 and second_arr.ndim == 2:
                    print("\nResult of Matrix Multiplication:\n", analyzer.matrix_multiply(second_arr))
                else:
                    print("\nResult of Dot Product:\n", analyzer.dot_product(second_arr))

        elif choice == '3':
            if analyzer.data is None:
                print("Please create an array first!")
                continue

            print("\nChoose an option:")
            print("1. Combine Arrays")
            print("2. Split Array")
            sub_choice = input("Enter your choice: ").strip()

            if sub_choice == '1':
                total_elem = analyzer.data.size
                raw = input(f"\nEnter the elements of another array to combine ({total_elem} elements separated by space): ")
                vals = [float(x) if '.' in x else int(x) for x in raw.split()][:total_elem]
                second_arr = np.array(vals).reshape(analyzer.data.shape)

                print("\nOriginal Array:\n", analyzer.data)
                print("Second Array:\n", second_arr)
                combined = analyzer.combine(second_arr, axis=0)
                print("\nCombined Array (Vertical Stack):\n", combined)
            elif sub_choice == '2':
                sec = int(input("Enter number of splits: "))
                splits = analyzer.split(sec, axis=0)
                print("\nSplits:")
                for i, s in enumerate(splits, 1):
                    print(f"Split {i}:\n{s}")

        elif choice == '4':
            if analyzer.data is None:
                print("Please create an array first!")
                continue

            print("\nChoose an option:")
            print("1. Search a value")
            print("2. Sort the array")
            print("3. Filter values")
            sub_choice = input("Enter your choice: ").strip()

            if sub_choice == '1':
                val = float(input("Enter value to search: "))
                indices = analyzer.search_value(val)
                print(f"Value found at indices: {indices}")
            elif sub_choice == '2':
                print("\nOriginal Array:\n", analyzer.data)
                sorted_arr = analyzer.sort_array(axis=-1)
                print("\nSorted Array:\n", sorted_arr)
                print("(Sorting applied row-wise.)")
            elif sub_choice == '3':
                cond = input("Enter filter condition (e.g., > 20): ").strip()
                filtered = analyzer.filter_values(cond)
                print("\nFiltered Array Elements:\n", filtered)

        elif choice == '5':
            if analyzer.data is None:
                print("Please create an array first!")
                continue

            print("\nChoose an aggregate/statistical operation:")
            print("1. Sum")
            print("2. Mean")
            print("3. Median")
            print("4. Standard Deviation")
            print("5. Variance")
            print("6. Min & Max")
            print("7. Percentile")
            stat_choice = input("Enter your choice: ").strip()

            print("\nOriginal Array:\n", analyzer.data)

            if stat_choice == '1':
                print(f"\nSum of Array: {analyzer.get_sum()}")
            elif stat_choice == '2':
                print(f"\nMean of Array: {analyzer.get_mean()}")
            elif stat_choice == '3':
                print(f"\nMedian of Array: {analyzer.get_median()}")
            elif stat_choice == '4':
                print(f"\nStandard Deviation of Array: {analyzer.get_std()}")
            elif stat_choice == '5':
                print(f"\nVariance of Array: {analyzer.get_variance()}")
            elif stat_choice == '6':
                print(f"\nMinimum Value: {analyzer.get_min()}")
                print(f"Maximum Value: {analyzer.get_max()}")
            elif stat_choice == '7':
                p = float(input("Enter percentile value (0-100): "))
                print(f"\n{p}th Percentile: {analyzer.get_percentile(p)}")

        elif choice == '6':
            print("\nThank you for using the NumPy Analyzer!\nGoodbye!")
            break
        else:
            print("Invalid choice, please select between 1 and 6.")


if __name__ == "__main__":
    main()