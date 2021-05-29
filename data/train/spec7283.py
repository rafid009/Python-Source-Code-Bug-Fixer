import numpy as np 

def function(x):

	t5 = 2
	p6 = x
	paths = []
	try:
		if p6 <= 8:
			p6 = p6+x
			t5 = t5*4
			paths.append(1)
		else:
			t5 = t5-5
			p6 = 9*p6
			paths.append(2)
		if t5 >= 1:
			p6 = p6+8
			t5 = 8/7
			paths.append(3)
		else:
			x = 0/x
			p6 = 4*p6
			x = t5+p6
			paths.append(4)
		paths.append(5)
		assert t5 >= 0
		t5 = t5**0.5
		return t5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))