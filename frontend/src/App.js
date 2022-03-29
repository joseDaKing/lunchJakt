import { SearchField, Avatar, Collapsible } from "./components";



function App() {
  return (
    <div>
      <div 
      className="p-4 px-8 bg-blue-500 flex items-center justify-start">
        <Avatar
        className="ml-auto"
        url={"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSRLRn2eroO_vViw3n23fWTyM0kE67YyOdhkg&usqp=CAU"}/>
        
        <SearchField 
        className="ml-8 w-full max-w-3xl mr-auto"
        items={[
          "abra",
          "ibra",
          "asma",
          "isma"
        ]}/>
      </div>

      <div
      className="w-full flex flex-row gap-8 items-start mt-8 px-12">
        <div 
        className="w-1/3 space-y-4 h-fit">
          {Array(3).fill("").map((_, i) => (
            <Collapsible 
            key={i}
            label={`Resturang ${i+1}`}>
              <div
              className=" text-neutral-600">
                Överig information om 
                restaurangen som distans,
                pris, vilken typ av mat samt
                eventuellt om det finns studentrabbat.
              </div>
            </Collapsible>
          ))}
        </div>
        
        <div
        className="w-2/4 h-80 rounded-sm bg-neutral-400"/>
      </div>
    </div>
  );
}

export default App;
