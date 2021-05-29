import numpy as np 

def function(x):

	d2 = 5
	t3 = 2
	paths = []
	try:
		if x < 5:
			t3 = d2+4
			paths.append(1)
		else:
			x = x+t3
			d2 = 2*9
			d2 = d2/2
			paths.append(2)
		if x <= 4:
			x = 8*x
			d2 = 0-x
			t3 = d2+t3
			paths.append(3)
		else:
			d2 = d2*8
			d2 = 3+9
			t3 = t3+x
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		t3 = d2**0.5
		return t3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))