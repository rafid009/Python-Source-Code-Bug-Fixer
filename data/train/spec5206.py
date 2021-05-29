import numpy as np 

def function(x):

	t3 = x
	p2 = 3
	paths = []
	try:
		if t3 <= 4:
			t3 = p2+4
			paths.append(1)
		else:
			t3 = t3+0
			paths.append(2)
		if t3 < 6:
			x = x*t3
			p2 = 9/7
			t3 = p2-t3
			paths.append(3)
		else:
			t3 = t3*3
			paths.append(4)
		paths.append(5)
		assert t3 >= 0
		x = t3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))