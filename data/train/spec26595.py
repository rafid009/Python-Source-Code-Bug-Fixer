import numpy as np 

def function(x):

	u3 = 5
	t5 = 8
	paths = []
	try:
		if x >= 7:
			x = x+8
			u3 = 3-1
			u3 = u3/9
			paths.append(1)
		else:
			t5 = 7+8
			x = t5*x
			u3 = u3/7
			paths.append(2)
		if u3 < 7:
			t5 = t5-6
			t5 = t5+6
			t5 = x/1
			paths.append(3)
		else:
			u3 = x/6
			t5 = 7+t5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t5 = x**0.5
		return t5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))