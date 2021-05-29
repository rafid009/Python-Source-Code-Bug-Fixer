import numpy as np 

def function(x):

	t5 = x
	g1 = 4
	paths = []
	try:
		if x > 7:
			g1 = x/t5
			x = 5+0
			paths.append(1)
		else:
			x = 6+6
			paths.append(2)
		if x <= 0:
			t5 = g1+g1
			g1 = 3*g1
			x = x*1
			paths.append(3)
		else:
			g1 = x/g1
			g1 = g1/3
			paths.append(4)
		paths.append(5)
		assert t5 >= 0
		g1 = t5**0.5
		return g1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))