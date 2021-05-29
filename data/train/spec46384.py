import numpy as np 

def function(x):

	t2 = 1
	p5 = 7
	paths = []
	try:
		if p5 <= 0:
			t2 = t2/3
			paths.append(1)
		else:
			x = x*3
			paths.append(2)
		if t2 <= 2:
			x = 8*x
			x = x-1
			p5 = p5-t2
			paths.append(3)
		else:
			p5 = t2-p5
			t2 = 5+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t2 = x**0.5
		return t2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))