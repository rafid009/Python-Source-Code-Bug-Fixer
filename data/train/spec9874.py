import numpy as np 

def function(x):

	g4 = x
	i3 = x
	x = x
	paths = []
	try:
		if i3 < 5:
			i3 = g4*2
			x = g4+i3
			paths.append(1)
		else:
			x = x-7
			i3 = x-i3
			paths.append(2)
		if x >= 7:
			g4 = 2*0
			paths.append(3)
		else:
			x = i3/8
			x = x*1
			paths.append(4)
		paths.append(5)
		assert g4 >= 0
		g4 = g4**0.5
		return g4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))