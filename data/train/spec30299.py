import numpy as np 

def function(x):

	b6 = 2
	g1 = x
	x = 1
	paths = []
	try:
		if x <= 7:
			b6 = 3+5
			paths.append(1)
		else:
			x = b6/9
			x = x*4
			b6 = 8*2
			paths.append(2)
		if b6 > 2:
			x = x/1
			b6 = x*3
			b6 = x+g1
			paths.append(3)
		else:
			x = 9-x
			x = 5/7
			paths.append(4)
		paths.append(5)
		assert g1 >= 0
		b6 = g1**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))