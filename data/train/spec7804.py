import numpy as np 

def function(x):

	g3 = 7
	v2 = 0
	paths = []
	try:
		if g3 <= 2:
			v2 = x/v2
			v2 = v2+0
			x = x-2
			paths.append(1)
		else:
			g3 = 0*v2
			x = x+1
			x = x*6
			paths.append(2)
		if v2 > 9:
			g3 = 6-g3
			g3 = g3+5
			v2 = 9*5
			paths.append(3)
		else:
			v2 = v2+9
			x = 4-1
			g3 = g3-2
			paths.append(4)
		paths.append(5)
		assert g3 >= 0
		v2 = g3**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))