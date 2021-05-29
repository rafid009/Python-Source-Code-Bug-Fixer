import numpy as np 

def function(x):

	f0 = 2
	g8 = x
	paths = []
	try:
		if x > 1:
			g8 = g8*0
			f0 = f0/f0
			g8 = 4*g8
			paths.append(1)
		else:
			f0 = 3*8
			g8 = 1-f0
			paths.append(2)
		if x >= 6:
			f0 = g8/1
			x = x*4
			paths.append(3)
		else:
			x = g8/f0
			x = x+8
			paths.append(4)
		paths.append(5)
		assert g8 >= 0
		f0 = g8**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))