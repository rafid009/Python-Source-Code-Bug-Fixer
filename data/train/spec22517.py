import numpy as np 

def function(x):

	g5 = x
	p3 = x
	paths = []
	try:
		if x <= 3:
			g5 = g5+x
			g5 = g5+0
			paths.append(1)
		else:
			g5 = x+9
			p3 = p3-0
			x = 7-p3
			paths.append(2)
		if x > 9:
			x = x+x
			paths.append(3)
		else:
			p3 = g5/1
			p3 = p3-5
			g5 = x*p3
			paths.append(4)
		paths.append(5)
		assert g5 >= 0
		p3 = g5**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))