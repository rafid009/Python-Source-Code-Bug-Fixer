import numpy as np 

def function(x):

	p3 = x
	t7 = 7
	paths = []
	try:
		if p3 <= 3:
			t7 = 9+t7
			t7 = x+p3
			p3 = p3+t7
			paths.append(1)
		else:
			t7 = 4/t7
			t7 = 6-t7
			t7 = t7*9
			paths.append(2)
		if x <= 2:
			t7 = 2*t7
			paths.append(3)
		else:
			p3 = x/7
			x = x/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p3 = x**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))