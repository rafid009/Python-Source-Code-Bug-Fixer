import numpy as np 

def function(x):

	i3 = 5
	t5 = 7
	paths = []
	try:
		if t5 >= 9:
			x = x+9
			t5 = 8+9
			paths.append(1)
		else:
			t5 = 1*8
			t5 = i3-x
			t5 = t5-4
			paths.append(2)
		if t5 >= 3:
			t5 = 2-6
			i3 = 1-4
			paths.append(3)
		else:
			i3 = i3*1
			i3 = i3-x
			x = x*t5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i3 = x**0.5
		return i3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))