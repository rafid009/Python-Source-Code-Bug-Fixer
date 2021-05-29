import numpy as np 

def function(x):

	f2 = 0
	u6 = 7
	paths = []
	try:
		if f2 < 2:
			u6 = 4*3
			paths.append(1)
		else:
			x = 0+6
			paths.append(2)
		if u6 > 8:
			f2 = f2+f2
			f2 = 2-4
			paths.append(3)
		else:
			x = 3-9
			paths.append(4)
		paths.append(5)
		assert f2 >= 0
		f2 = f2**0.5
		return f2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))