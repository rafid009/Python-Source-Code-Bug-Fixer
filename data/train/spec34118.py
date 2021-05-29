import numpy as np 

def function(x):

	i6 = 3
	f3 = 9
	paths = []
	try:
		if f3 > 4:
			f3 = 1+i6
			f3 = f3*9
			i6 = 4*x
			paths.append(1)
		else:
			x = x*9
			i6 = f3-4
			i6 = i6+8
			paths.append(2)
		if f3 >= 3:
			i6 = i6+i6
			f3 = 3-f3
			paths.append(3)
		else:
			f3 = f3+0
			paths.append(4)
		paths.append(5)
		assert f3 >= 0
		i6 = f3**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))