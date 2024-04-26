
namespace visual_console
{

    internal class String_Indexerr
    {
        private string[] arrS=new string[10];

        public string this[int index]
        {
            get
            {
                if (index < 0 || index >= arrS.Length)
                    throw new ArgumentOutOfRangeException("Index is out of the range in get");
                return arrS[index];
            }

            set
            {
                if (index < 0 || index >= arrS.Length)
                    throw new IndexOutOfRangeException("Index is out of the range in set");
                arrS[index] = value;
            }
        }
    }
}

