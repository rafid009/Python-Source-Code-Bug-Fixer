import numpy as np 

def function(x):

	t5 = 5
	p5 = x
	x = 8
	paths = []
	try:
		if p5 > 1:
			x = x/x
			paths.append(1)
		else:
			x = p5*x
			t5 = 4-3
			x = 2+8
			paths.append(2)
		if t5 > 4:
			t5 = 3+t5
			t5 = t5*7
			paths.append(3)
		else:
			t5 = t5-6
			paths.append(4)
		paths.append(5)
		assert p5 >= 0
		t5 = p5**0.5
		return t5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))