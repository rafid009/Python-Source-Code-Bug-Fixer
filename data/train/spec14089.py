import numpy as np 

def function(x):

	t3 = 0
	p5 = x
	x = 4
	paths = []
	try:
		if t3 <= 1:
			t3 = t3*4
			x = 6*p5
			x = 4+x
			paths.append(1)
		else:
			t3 = 1-x
			x = 5*x
			x = x+4
			paths.append(2)
		if x < 2:
			x = 4-x
			paths.append(3)
		else:
			t3 = 8*p5
			t3 = t3/x
			paths.append(4)
		paths.append(5)
		assert p5 >= 0
		t3 = p5**0.5
		return t3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))