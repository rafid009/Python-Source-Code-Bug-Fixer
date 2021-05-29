import numpy as np 

def function(x):

	f0 = 9
	t5 = x
	paths = []
	try:
		if f0 <= 9:
			t5 = 3-x
			f0 = x*8
			paths.append(1)
		else:
			x = t5/x
			t5 = f0+0
			f0 = f0/x
			paths.append(2)
		if f0 >= 7:
			t5 = t5/4
			f0 = 2/3
			paths.append(3)
		else:
			x = x/x
			f0 = x+9
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