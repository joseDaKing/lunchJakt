export const Avatar = ({ 
    url, 
    className
}) => {

    return (
        <div
        className={`h-10 w-10 rounded-full bg-white overflow-hidden cursor-pointer object-center ${className??""}`}>
            <img
            className="object-cover block w-full h-full"
            src={url}/>
        </div>
    );
}