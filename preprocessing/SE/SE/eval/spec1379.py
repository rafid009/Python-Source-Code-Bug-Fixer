import numpy as np 

def function(x):

	g9 = 9
	f0 = 2
	paths = []
	try:
		if f0 <= 3:
			g9 = 3*2
			f0 = g9-x
			paths.append(1)
		else:
			x = g9+f0
			f0 = f0*6
			x = x-x
			paths.append(2)
		if x >= 8:
			x = 2+3
			paths.append(3)
		else:
			g9 = 4/f0
			f0 = 7*4
			paths.append(4)
		paths.append(5)
		assert g9 >= 0
		f0 = g9**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))