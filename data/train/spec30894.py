import numpy as np 

def function(x):

	i0 = x
	f3 = x
	paths = []
	try:
		if i0 <= 4:
			i0 = i0+f3
			x = x-f3
			paths.append(1)
		else:
			f3 = f3+i0
			x = x/x
			paths.append(2)
		if x >= 7:
			f3 = 5-f3
			i0 = 5*x
			f3 = 0*4
			paths.append(3)
		else:
			x = x*9
			paths.append(4)
		paths.append(5)
		assert f3 >= 0
		f3 = f3**0.5
		return f3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))