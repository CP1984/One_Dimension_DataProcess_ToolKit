import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

class OneDimensionDataProcessToolKit:
    def __init__(self, x, y):
        """
        Initializes the LinearInterpolator with data points (x, y).

        Args:
            x (array-like): Original x values.
            y (array-like): Original y values.
        """
        self.x = x
        self.y = y

    def interpolate(self, num_points, custom_limits=False, lower_limit=None, upper_limit=None, plot=False):
        """
        Performs linear interpolation and returns the interpolated y values.

        Args:
            num_points (int): Number of points for interpolation.
            custom_limits (bool): Whether to use custom lower and upper limits.
            lower_limit (float): Custom lower limit for interpolation.
            upper_limit (float): Custom upper limit for interpolation.
            plot (bool): Whether to plot the interpolated data.

        Returns:
            array-like: Interpolated y values.
        """
        if custom_limits:
            new_x = np.linspace(lower_limit, upper_limit, num_points)
        else:
            new_x = np.linspace(self.x[0], self.x[-1], num_points)

        interp_func = interp1d(self.x, self.y, kind='linear')
        interpolated_y = interp_func(new_x)

        if plot:
            self._plot_interpolation(new_x, interpolated_y)

        return interpolated_y

    def _plot_interpolation(self, new_x, interpolated_y):
        plt.figure(figsize=(8, 6))
        plt.scatter(self.x, self.y, label='Original trace', color='blue')
        plt.plot(new_x, interpolated_y, label='Interpolation', color='red')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Linear interpolation')
        plt.legend()
        plt.grid(True)
        plt.show()

if __name__ == "__main__":
    # Example usage
    x_data = np.array([0, 1, 2, 3, 4, 5])
    y_data = np.array([0, 2, 3, 1, 4, 5])

    # Create an instance of LinearInterpolator
    interpolator = OneDimensionDataProcessToolKit(x_data, y_data)

    # Interpolate with default limits and plot the data
    interpolated_y_default = interpolator.interpolate(num_points=100, plot=True)

    # Interpolate with custom limits (1 to 4) without plotting
    interpolated_y_custom = interpolator.interpolate(num_points=100, custom_limits=True, lower_limit=0.5, upper_limit=3.5, plot=True)