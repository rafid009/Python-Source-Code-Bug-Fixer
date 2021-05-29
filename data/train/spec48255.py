import numpy as np 

def function(x):

	b2 = 5
	g5 = x
	paths = []
	try:
		if x <= 8:
			x = 6/b2
			x = 8+0
			x = x+b2
			paths.append(1)
		else:
			g5 = g5/g5
			g5 = b2/5
			paths.append(2)
		if g5 >= 2:
			b2 = x/5
			paths.append(3)
		else:
			x = 7*0
			paths.append(4)
		paths.append(5)
		assert g5 >= 0
		b2 = g5**0.5
		return b2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))