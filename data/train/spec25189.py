import numpy as np 

def function(x):

	f3 = x
	g2 = x
	paths = []
	try:
		if x > 8:
			g2 = 3*g2
			f3 = 5*0
			x = x*1
			paths.append(1)
		else:
			g2 = g2*4
			paths.append(2)
		if x <= 7:
			x = 8*8
			x = x/f3
			paths.append(3)
		else:
			f3 = 6-x
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