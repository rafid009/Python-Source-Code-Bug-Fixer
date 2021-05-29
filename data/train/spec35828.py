import numpy as np 

def function(x):

	t1 = x
	p2 = x
	paths = []
	try:
		if x < 9:
			x = p2/x
			t1 = 1+3
			x = 6-6
			paths.append(1)
		else:
			x = x/9
			t1 = t1+3
			paths.append(2)
		if p2 > 3:
			p2 = 8+p2
			t1 = 3-p2
			p2 = p2*8
			paths.append(3)
		else:
			x = x+x
			paths.append(4)
		paths.append(5)
		assert t1 >= 0
		t1 = t1**0.5
		return t1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))