import numpy as np 

def function(x):

	p3 = 8
	t7 = 8
	paths = []
	try:
		if p3 > 0:
			x = x+x
			t7 = t7/x
			paths.append(1)
		else:
			p3 = p3/6
			p3 = p3-6
			paths.append(2)
		if p3 < 9:
			p3 = 5*p3
			t7 = t7/9
			p3 = 1*x
			paths.append(3)
		else:
			p3 = p3*9
			p3 = p3*1
			paths.append(4)
		paths.append(5)
		assert t7 >= 0
		x = t7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))