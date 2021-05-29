import numpy as np 

def function(x):

	i3 = x
	f3 = 4
	paths = []
	try:
		if x <= 0:
			f3 = x*f3
			paths.append(1)
		else:
			f3 = 9/f3
			paths.append(2)
		if i3 > 7:
			i3 = 3*i3
			f3 = 3+0
			paths.append(3)
		else:
			x = 0/x
			x = x*i3
			f3 = f3-5
			paths.append(4)
		paths.append(5)
		assert f3 >= 0
		x = f3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))