import numpy as np 

def function(x):

	b5 = x
	t3 = 9
	paths = []
	try:
		if b5 < 1:
			t3 = 0*t3
			t3 = t3+x
			paths.append(1)
		else:
			x = x+4
			paths.append(2)
		if b5 < 5:
			t3 = 5/t3
			paths.append(3)
		else:
			x = x/9
			paths.append(4)
		paths.append(5)
		assert b5 >= 0
		t3 = b5**0.5
		return t3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))