import numpy as np 

def function(x):

	m9 = x
	t7 = x
	x = x
	paths = []
	try:
		if x < 2:
			t7 = t7+6
			paths.append(1)
		else:
			x = x-4
			x = x/1
			x = t7+1
			paths.append(2)
		if m9 <= 3:
			x = m9/8
			x = x+t7
			x = m9/x
			paths.append(3)
		else:
			t7 = t7+x
			x = t7+x
			x = 0/x
			paths.append(4)
		paths.append(5)
		assert m9 >= 0
		t7 = m9**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))